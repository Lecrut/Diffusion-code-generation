def feet_to_inches(feet_value):
    inches_value = feet_value * 12
    return inches_value

if __name__ == '__main__':
    feet_input = 5
    result = feet_to_inches(feet_input)
    print(result)