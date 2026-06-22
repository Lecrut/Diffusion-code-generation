def feet_to_inches(feet):
    return feet * 12

if __name__ == '__main__':
    sample_feet = [1, 5, 10, 25.5, 100]
    for f in sample_feet:
        print(feet_to_inches(f))