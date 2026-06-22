INCHES_PER_FOOT = 12

def feet_to_inches(feet):
    return feet * INCHES_PER_FOOT

def main():
    test_value = 15
    output = feet_to_inches(test_value)
    print(output)

if __name__ == '__main__':
    main()