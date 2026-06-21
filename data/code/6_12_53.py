def calculate_weight_difference(weight1, weight2):
    return abs(weight1 - weight2)

if __name__ == '__main__':
    person1_weight = 85.0
    person2_weight = 79.2
    difference = calculate_weight_difference(person1_weight, person2_weight)
    print(f"The weight difference is: {difference}")