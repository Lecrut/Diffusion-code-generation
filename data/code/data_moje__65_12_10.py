INCHES_PER_FOOT = 12

def feet_to_inches(feet):
    return feet * INCHES_PER_FOOT

if __name__ == '__main__':
    foot_value = 10
    result = feet_to_inches(foot_value)
    print(result)