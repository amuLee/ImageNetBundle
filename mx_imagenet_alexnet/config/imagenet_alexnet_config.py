# import the necessary packages
from os import path 

# define the bash path to where the ImageNet dataset
# devkit are stored on disk)
BASH_PATH = "/home/amu/raid/datasets/imagenet/ILSVRC2015"

# based on the bash path, derive the images bash path, image sets
# path, and devkit path 
IMAGES_PATH = path.sep.join([BASH_PATH, "Data/CLS-LOC"])
IMAGE_SETS_PATH = path.sep.join([BASH_PATH, "ImageSets/CLS-LOC/"])
DEVKIT_PATH = path.sep.join([BASH_PATH, "devkit/data"])

# define the path that maps the 1,000 possible WordNet IDs to the 
# class label integers
WORD_IDS = path.sep.join([DEVKIT_PATH, "map_clsloc.txt"])

# define the paths to the training file that maps the (partial)
# image filename to integer class label 
TRAIN_LIST = path.sep.join([IMAGE_SETS_PATH, "train_cls.txt"])

# define the paths to the validation filenames along with the 
# file that contains the ground-truth validation labels
VAL_LIST = path.sep.join([IMAGE_SETS_PATH, "val.txt"])
VAL_LABELS = path.sep.join([DEVKIT_PATH,
    "ILSVRC2015_clsloc_validation_ground_truth.txt"])

# define the path to the validation files that are blacklisted
VAL_BLACKLIST = path.sep.join([DEVKIT_PATH,
    "ILSVRC2015_clsloc_validation_blacklist.txt"])

# since we do not have access to the testing data we need to 
# take a number of images from the training data and use it instead
NUM_CLASSES = 1000
NUM_TEST_IMAGES = 50 * NUM_CLASSES 

# define the path to the output training, validation, and testing
# lists
MX_OUTPUT = "/home/amu/raid/datasets/imagenet"
TRAIN_MX_LIST = path.sep.join([MX_OUTPUT, "lists/train.lst"])
VAL_MX_LIST = path.sep.join([MX_OUTPUT, "lists/val.lst"])
TEST_MX_LIST = path.sep.join([MX_OUTPUT, "lists/test.lst"])

# define the path to the output training, validation, and testing
# image records
TRAIN_MX_REC = path.sep.join([MX_OUTPUT, "rec/train.rec"])
VAL_MX_REC = path.sep.join([MX_OUTPUT, "rec/val.rec"])
TEST_MX_REC = path.sep.join([MX_OUTPUT, "rec/test.rec"])

# define the path to the dataset mean
DATASET_MEAN = "output/imagenet_mean.json"

# define the batch size and number of devices used for training
BATCH_SIZE = 128
NUM_DEVICES = 1
