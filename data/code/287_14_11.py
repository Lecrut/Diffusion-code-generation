def compare_weights(weight1, unit1, weight2, unit2):
    conversion = {'kg': 1, 'lbs': 0.453592}
    weight1_converted = weight1 * conversion[unit1]
    weight2_converted = weight2 * conversion[unit2]
    
    if weight1_converted > weight2_converted:
        return f"{weight1} {unit1} is heavier than {weight2} {unit2}"
    elif weight1_converted < weight2_converted:
        return f"{weight2} {unit2} is heavier than {weight1} {unit1}"
    else:
        return f"{weight1} {unit1} and {weight2} {unit2} are equal"

if __name__ == '__main__':
    print(compare_weights(70, 'kg', 154, 'lbs'))
    print(compare_weights(60, 'kg', 130, 'lbs'))
    print(compare_weights(80, 'kg', 80, 'kg'))