def repeat_action(count):
    if count < 0:
        raise ValueError("Count must be a non-negative integer")
    result = ""
    while count > 0:
        result += "Action "
        count -= 1
    return result.strip()

if __name__ == '__main__':
    number_of_repeats = 100
    output = repeat_action(number_of_repeats)
    print(output)