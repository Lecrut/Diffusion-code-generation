import math

def calculate_area_from_config(config):
    return math.pi * config['radius'] ** 2

if __name__ == '__main__':
    sample_config = {'radius': 3}
    area = calculate_area_from_config(sample_config)
    print(area)