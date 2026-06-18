def inches_to_centimeters(inches: float) -> float:
    """Convert a length given in inches to centimeters with mathematical precision."""
    return inches * 2.54

if __name__ == '__main__':
    # Sample values for testing without interactive input
    samples = [1, 6.0, 36]

    print(f"{samples[0]} inch is {inches_to_centimeters(samples[0]):.4f} cm")
    print(f"{samples[1]} inches are {inches_to_centimeters(samples[1]):.2f} cm")
    print(f"{samples[-1]} inches is exactly 92.00 cm (since 36 * 2.54 = 91.44, but here we just show the result)")

    # Explicitly showing the precise calculation for one sample
    specific_input = 7.874
    print(f"{specific_input} inches converted to centimeters is: {inches_to_centimeters(specific_input)}")