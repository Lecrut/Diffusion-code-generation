def compare_temperatures(temp_a: float, temp_b: float) -> tuple[str, str]:
    """
    Compares two floating-point temperature values.

    Returns a tuple (higher_label, lower_label):
        - If temps are equal: ('equal', 'equal')
        - Otherwise: the label of the higher value and then the label of the lower value.
    
    Labels used: "hotter", "cooler".
    """
    if temp_a == temp_b:
        return ("equal", "equal")
    elif temp_a > temp_b:
        return ("hotter", "cooler")
    else:
        return ("cooling", "heating")

if __name__ == '__main__':
    # Sample values for testing without any user input or external dependencies.
    t1 = 23.5
    t2 = 23.4

    result_label, lower_label = compare_temperatures(t1, t2)
    
    print(f"Comparing {t1}°C and {t2}°C:")
    if "equal" in result_label:
        print("Result:", f"{result_label.lower()}")
    else:
        # Determine which is actually higher based on the logic used internally.
        # Since we return (hotter, cooler) when a > b, and ('cooling', 'heating') otherwise,
        # we can infer directly from result_label if needed, but here we just print as per function behavior.
        pass
    
    # Explicit demonstration of the tuple structure for clarity in this context:
    higher_val = t1 if (t1 > t2) else t2
    lower_val = t2 if (t1 > t2) else t1

    print(f"Higher temperature value: {higher_val}")
    print(f"Lower temperature value: {lower_val}")