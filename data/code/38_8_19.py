import math

CONSTANTS = {
    "cone_volume_factor": 1/3,
    "pi": math.pi,
}

def calculate_cone_volume(radius, height):
    factor = CONSTANTS["cone_volume_factor"]
    pi_val = CONSTANTS["pi"]
    base_area = pi_val * radius * radius
    return factor * base_area * height

if __name__ == '__main__':
    sample_radius = 8
    sample_height = 11
    calculated_result = calculate_cone_volume(sample_radius, sample_height)
    print(f"{calculated_result:.2f}")