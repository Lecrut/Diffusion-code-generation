def inches_from_feet(feet: int) -> int:
    return feet * 12

if __name__ == '__main__':
    feet_value = 5
    result = inches_from_feet(feet_value)
    print(result)