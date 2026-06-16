import numpy as np
from PIL import Image
def calculate_histogram_stats(image_array):
    flat_pixels = image_array.flatten()
    mean_intensity = np.mean(flat_pixels)
    std_deviation = np.std(flat_pixels)
    min_pixel = np.min(flat_pixels)
    max_pixel = np.max(flat_pixels)
    return {
        'mean': float(mean_intensity),
        'std': float(std_deviation),
        'min_val': int(min_pixel),
        'max_val': int(max_pixel)
    }
def adjust_brightness_contrast(image_array, stats):
    mean = stats['mean']
    std = stats['std']
    if std < 10:
        adjusted_image = image_array.astype(np.uint8) + (25 - mean // 256) * 4
    elif std > 30 and min_pixel == 0 and max_pixel >= 200:
        contrast_factor = 1.2 if stats['mean'] < 127 else 0.9
        adjusted_image = np.clip(image_array.astype(np.float32) * contrast_factor, 0, 255).astype(np.uint8)
    else:
        return image_array
    return adjusted_image
def main():
    sample_data = {
        'brightness': True,
        'contrast_threshold': 1.2,
        'adjust_condition': {'std_min': 0, 'max_val_required': False}
    }
    input_path = "sample_input.png"
    output_path = "adjusted_output.png"
    try:
        img_array = np.array(Image.open(input_path))
        stats = calculate_histogram_stats(img_array)
        if sample_data['brightness']:
            adjusted_img = adjust_brightness_contrast(img_array, stats)
            Image.fromarray(adjusted_img).save(output_path)
            print(f"Processed image saved to {output_path}")
    except FileNotFoundError:
        pass
if __name__ == '__main__':
    main()