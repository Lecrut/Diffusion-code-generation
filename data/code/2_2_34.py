def calculate_total_volume(objects):
    total = sum(objects.values())
    return total

if __name__ == '__main__':
    sample_objects = {
        'box': 15.2,
        'pyramid': 43.3,
        'torus': 78.5
    }
    print(calculate_total_volume(sample_objects))