def feet_to_micrometers(feet):
    conversion_factor = 304800
    micrometers = feet * conversion_factor
    return micrometers

if __name__ == '__main__':
    sample_feet = [1, 5, 10]
    for feet in sample_feet:
        result = feet_to_micrometers(feet)
        print(f"{feet} feet is equal to {result} micrometers")