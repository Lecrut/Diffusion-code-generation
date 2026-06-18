import numpy as np
from PIL import Image
def analyze_histogram(image):
    pixels = list(image.getdata())
    flat_array = np.array(pixels)
    intensity_distribution = np.histogram(flat_array)[0]
    mean_intensity = float(np.mean(flat_array))
    std_deviation = float(np.std(flat_array))
    return {
        'mean': mean_intensity,
        'std': std_deviation,
        'histogram': intensity_distribution
    }
def adjust_brightness_contrast(image, params):
    width, height = image.size
    new_pixels = []
    for x in range(width):
        for y in range(height):
            pixel_data = list(image.getpixel((x, y)))
            if len(pixel_data) == 1:
                gray_val = np.array(pixel_data)[0]
                adjusted_val = int(gray_val + params['brightness']) * (params['contrast'] / 256.0)
                new_pixels.append([adjusted_val])
            else:
                r, g, b = pixel_data
                factor_r = float(r) * (1 + params['contrast'] - 1) / 256.0
                adjusted_r = int(max(0, min(255, round(factor_r))))
                factor_g = float(g) * (1 + params['contrast'] - 1) / 256.0
                adjusted_g = int(max(0, min(255, round(factor_g))))
                factor_b = float(b) * (1 + params['contrast'] - 1) / 256.0
                adjusted_b = int(max(0, min(255, round(factor_b))))
                new_pixels.append([adjusted_r, adjusted_g, adjusted_b])
    return Image.new('RGB', image.size), new_pixels
def main():
    sample_image_path = 'sample_input.png'
    try:
        img = Image.open(sample_image_path)
        stats = analyze_histogram(img)
        brightness_threshold = 50.0
        contrast_multiplier = 128.0
        if (stats['mean'] > brightness_threshold and 
            stats['std'] < contrast_multiplier):
            adjusted_img, _ = adjust_brightness_contrast(img, {
                'brightness': -30,
                'contrast': 50
            })
            output_path = 'adjusted_output.png'
            adjusted_img.save(output_path)
        else:
            print("Statistical conditions not met. No adjustment performed.")
    except FileNotFoundError:
        pass
if __name__ == '__main__':
    main()