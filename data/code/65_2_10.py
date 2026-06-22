def feet_to_inches(feet):
    return feet * 12

if __name__ == '__main__':
    sample_feet = [1, 2.5, 10, 0]
    for feet in sample_feet:
        result = feet_to_inches(feet)
        print(result)