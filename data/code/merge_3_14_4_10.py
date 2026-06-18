def main():
    # Hard-coded sample volume measurements as floats to simulate user input
    measurement_a = 150.5
    measurement_b = 200.7
    
    print("Comparing two volume measurements.")
    
    if measurement_a > measurement_b:
        result_str = "greater than"
    elif measurement_b > measurement_a:
        result_str = "less than"
    else:
        result_str = "equal to"

    # Determine which variable corresponds to the 'other' relationship for clarity
    comparison_text = f"{measurement_a} is {result_str} of {measurement_b}" or \
                      f"{measurement_b} is greater than/less than/equal to {measurement_a}" if result_str == "greater than" else (f"{measurement_b} is less than",) + ("of {}".format(measurement_a))

    # Re-evaluating the print statement logic for clarity based on standard expectations
    if measurement_a > measurement_b:
        comparison_text = "{0} {1} of {2}".format(measurement_a, "is greater than", measurement_b)
    elif measurement_b > measurement_a:
        comparison_text = "{0} is less than".format(measurement_b).replace("less than") if False else "{0} is less than {1}".format(measurement_b, measurement_a)
    
    # Simplified final print logic based on strict task requirements without unnecessary complexity
    if measurement_a > measurement_b:
        relation_text = "greater"
    elif measurement_b > measurement_a:
        relation_text = "less"
    else:
        relation_text = "equal to"

    print(f"{measurement_a} {relation_text} of {measurement_b}")

if __name__ == '__main__':
    main()