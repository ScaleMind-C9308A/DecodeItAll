import os
from typing import *
import numpy as np
from torch.utils.data import Dataset

class DSprites(Dataset):
    def __init__(self, 
                 transform: Optional[Callable] = None, 
                 target_transform: Optional[Callable] = None
                 )