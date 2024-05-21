import torch
from torch import Tensor


class CustomImageSelector:
    """
    A custom node for ComfyUI that computes the top-left coordinates of a cropped bounding box given the dimension of the final cropping area.

    Class Methods:
    --------------
    INPUT_TYPES(cls) -> dict:
        A class method returning a dictionary containing configuration for input fields.

    Attributes:
    -----------
    RETURN_TYPES (tuple):
        Specifies the types of each element in the output tuple.
    FUNCTION (str):
        The name of the entry-point method.
    CATEGORY (str):
        Specifies the category the node should appear in the UI.
    """

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        """
        Returns a dictionary containing configuration for input fields.

        Returns:
        --------
        dict:
            A dictionary with keys specifying input fields and values specifying their types and default values.
        """
        return {
            "required": {
                "images": ("IMAGE",)
            },
        }

    RETURN_TYPES = ("IMAGE",)
    RETURN_NAMES = ("images",)
    FUNCTION = "select_one_image"
    CATEGORY = "CustomImageSelector"

    def select_one_image(self, images: Tensor):
        if isinstance(images, list):
            return images

        print(f"Input shape: {images.shape}")
        max_area = 0
        max_image = None
        for image in images:
            print(f"Shape: {image.shape}")
            area = image.shape[0] * image.shape[1]
            if area > max_area:
                max_area = area
                max_image = image

        print(f"Max area:{max_area} shape: {max_image.shape}")
        result = torch.stack([max_image], dim=0)
        print(f"New tensor shape: {result.shape}")
        return [result]


# Dictionary to map node classes to their names
NODE_CLASS_MAPPINGS = {
    "CustomImageSelector": CustomImageSelector
}

# Dictionary to map node names to their friendly display names
NODE_DISPLAY_NAME_MAPPINGS = {
    "CustomImageSelector": "Custom IMG selector Node"
}
