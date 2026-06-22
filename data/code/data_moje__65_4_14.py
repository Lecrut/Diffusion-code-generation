def foot_to_inches(feet_list):
    return [feet * 12 for feet in feet_list]

if __name__ == '__main__':
    feet_values = [1, 2.5, 10, 0.5]
    result = foot_to_inches(feet_values)
    print(result)