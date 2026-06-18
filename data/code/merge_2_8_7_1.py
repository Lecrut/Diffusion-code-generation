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
    if stats['std'] < 10:
        new_image = image.convert('L').point(lambda x: min(255, max(0, int(x + (stats['mean'] - 128)))))
        return Image.fromarray(np.array(new_image), 'I')
    elif stats['min'] < 30 or stats['max'] > 240:
        new_image = image.convert('L').point(lambda x: min(255, max(0, int(x * (1 + ((stats['mean'] - 128) / std_dev))))) if 'std' in locals() else None)
    return image
def main():
    img_path = "sample_input.png"
    try:
        with Image.open(img_path).convert('L') as original_image:
            stats = calculate_histogram_stats(original_image)
            adjusted_img = adjust_brightness_contrast(original_image, stats)
            output_name = f"{img_path}_processed.jpg"
            adjusted_img.save(output_name)
    except FileNotFoundError:
        print("Error: sample_input.png not found.")
if __name__ == '__main__':
    main()