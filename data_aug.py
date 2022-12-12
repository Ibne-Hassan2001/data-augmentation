from keras.preprocessing.image import ImageDataGenerator

# Construct an instance of the ImageDataGenerator class
# Pass the augmentation parameters through the constructor. 

datagen = ImageDataGenerator(
        rotation_range=45,     #Random rotation between 0 and 45
        width_shift_range=0.2,   #% shift
        height_shift_range=0.2,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True,
        vertical_flip = True,
        fill_mode='reflect') 


i = 0
for batch in datagen.flow_from_directory(directory='images/', 
                                         batch_size=700,  
                                         target_size=(150, 150),
                                         color_mode="rgb",
                                         save_to_dir='augmented', 
                                         save_prefix='aug', 
                                         save_format='png'):
    i += 1
    if i > 31:
        break 