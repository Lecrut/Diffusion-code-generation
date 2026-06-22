def feet_to_inches(feet_list):
    return [round(f * 12, 10) for f in feet_list]

if __name__ == '__main__':
    feet_values = [1.0, 2.5, 10.125, 0.1]
    result = feet_to_inches(feet_values)
    print(result)