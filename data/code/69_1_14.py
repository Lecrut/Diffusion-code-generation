def calculate_total_feet(miles):
    return [m * 5280 for m in miles]

if __name__ == '__main__':
    sample_miles = [1, 2.5, 10, 0.5, 100]
    feet_values = calculate_total_feet(sample_miles)
    print(feet_values)