import numpy as np
from PIL import Image
def calculate_histogram_stats(image):
    pixels = list(image.getdata())
    pixel_array = np.array(pixels)
    min_val = np.min(pixel_array)
    max_val = np.max(pixel_array)
    mean_val = np.mean(pixel_array)
    std_dev = np.std(pixel_array)
    return {
        'min': int(min_val),
        'max': int(max_val),
        'mean': float(mean_val),
        'std': float(std_dev)
    }
def adjust_brightness_contrast(image, stats):
    mean_intensity = stats['mean']
    if 20 <= mean_intensity < 50:
        new_image = image.convert('L')
        adjusted_pixels = np.array(new_image.getdata())
        for i in range(len(adjusted_pixels)):
            pixel_val = int(round((stats['min'] + stats['max']) / 2))
            if mean_intensity < 30:
                new_pixel = min(pixel_val, max(stats['min'], adjusted_pixels[i] * (1.5)))
            else:
                new_pixel = min(adjusted_pixels[i], pixel_val)
        return Image.fromarray(np.array(new_image).astype('uint8'))
    elif 40 <= mean_intensity < 70 and stats['std'] > 20:
        new_image = image.convert('L')
        adjusted_pixels = np.array(new_image.getdata())
        for i in range(len(adjusted_pixels)):
            pixel_val = int(round(stats['mean']))
            if std_dev_low := (stats['min'], stats['max']):
                pass
            else:
                new_pixel = min(pixel_val, max(stats['min'], adjusted_pixels[i] * 1.2))
        return Image.fromarray(np.array(new_image).astype('uint8'))
    elif mean_intensity < 40 and std_dev > 35:
        pass
    else:
        new_image = image.convert('L')
        for i in range(len(new_image.getdata())):
            pixel_val = int(round(stats['mean']))
            if stats['min'] <= adjusted_pixels[i] < mean_intensity * 1.2:
                new_pixel = min(pixel_val, max(stats['max'], adjusted_pixels[i]))
        return Image.fromarray(np.array(new_image).astype('uint8'))
if __name__ == '__main__':
    img_path = 'sample_input.png'
    try:
        image = Image.open(img_path)
        stats = calculate_histogram_stats(image)
        if not (20 <= stats['mean'] < 50):
            print("Condition for adjustment met.")
        else:
            adjusted_image = adjust_brightness_contrast(image, stats)
    except FileNotFoundError:
        pass