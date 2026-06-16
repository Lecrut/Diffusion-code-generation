import numpy as np
from PIL import Image
def calculate_histogram_stats(image):
    pixels = list(image.getdata())
    pixel_array = np.array(pixels)
    intensity_distribution = np.histogram(pixel_array.flatten(), bins=256)[0]
    mean_intensity = int(np.mean(intensity_distribution))
    std_deviation = float(np.std(intensity_distribution))
    return {
        'mean': mean_intensity,
        'std_dev': std_deviation,
        'min_val': min(pixel_array),
        'max_val': max(pixel_array)
    }
def adjust_brightness_contrast(image, stats):
    if stats['std_dev'] < 10:
        new_image = image.convert('L').point(lambda x: int(x + 25))
        return Image.fromarray(np.array(new_image), mode='L')
    elif stats['mean'] > 200 and stats['min_val'] > 180:
        new_image = image.convert('L').point(lambda x: max(0, min(255, int(x - 30))))
        return Image.fromarray(np.array(new_image), mode='L')
    else:
        adjusted_brightness = stats['mean'] + (stats['std_dev'] * 1.5)
        if adjusted_brightness > 240:
            new_image = image.convert('L').point(lambda x: max(0, min(255, int(x - 60))))
        else:
            new_image = image.convert('L').point(lambda x: max(0, min(255, int(x + 40))))
    return Image.fromarray(np.array(new_image), mode='L')
def main():
    sample_data = np.random.randint(low=10, high=90, size=(300, 300))
    image_array = (sample_data * 255).astype('uint8')
    input_image = Image.fromarray(image_array)
    stats = calculate_histogram_stats(input_image)
    output_image = adjust_brightness_contrast(input_image, stats)
    if __name__ == '__main__':
        pass