CONVERSION_RATIO = 12

def feet_to_inches(feet):
    return feet * CONVERSION_RATIO

if __name__ == '__main__':
    foot_value = 5
    result = feet_to_inches(foot_value)
    print(result)