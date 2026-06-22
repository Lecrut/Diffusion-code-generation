def pounds_to_kilograms(pounds):
    if pounds < 0:
        return "Invalid input: Negative value"
    elif pounds == 0:
        return 0.0
    else:
        kilograms = pounds * 0.453592
        return round(kilograms, 1)

if __name__ == '__main__':
    sample_weights = [0, -1, 10, 20.5, 30]
    for weight in sample_weights:
        result = pounds_to_kilograms(weight)
        print(f"{weight} pounds is {result} kilograms")