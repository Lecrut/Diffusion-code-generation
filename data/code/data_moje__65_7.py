def feet_to_inches(feet):
    return feet * 39.3701

if __name__ == '__main__':
    sample_feet = [1, 5.5, 10, 0, -3]
    for f in sample_feet:
        print(feet_to_inches(f))