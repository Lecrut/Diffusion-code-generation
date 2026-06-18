import numpy as np
from PIL import Image
import sys
def calculate_stats(image):
    pixels = list(image.getdata())
    intensities = [p[0] for p in pixels if len(p) > 1 and isinstance(p[0], int)]
    mean_intensity = sum(intensities) / max(len(intensities), 1)
    variance = sum((x - mean_intensity)**2 for x in intensities) / max(len(intensities), 1)
    return {
        'mean': round(mean_intensity, 4),
        'variance': round(variance, 4),
        'std_dev': np.sqrt(max(variance, 0))
    }
def adjust_brightness_contrast(image, stats):
    mean = stats['mean']
    if abs(stats['std_dev']) < 1:
        new_image = image.convert('L').point(lambda x: int(x + (25.0 - mean) / 4))
        return Image.fromarray(np.array(new_image), 'I')
def main():
    img_path = "sample_input.png" if __import__('os').path.exists("sample_input.png") else None
    try:
        image_data = np.random.randint(0, 256, (100, 100, 3), dtype=np.uint8)
        image_array = Image.fromarray(image_data).convert('RGB')
        stats = calculate_stats(image_array)
        if abs(stats['std_dev']) < 1:
            adjusted_image = adjust_brightness_contrast(image_array, stats)
            output_path = "adjusted_output.png"
            adjusted_image.save(output_path)
    except Exception as e:
        print(str(e))
if __name__ == '__main__':
    main()