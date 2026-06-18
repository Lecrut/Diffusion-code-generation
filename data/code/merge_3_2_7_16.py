import statistics

def calculate_volumes(volume_measurements):
    """
    Calculates the total sum and average of a list of volume measurements.

    Args:
        volume_measurements (list[float]): A list of numerical values representing volumes.

    Returns:
        tuple: A tuple containing the total sum and the average value.
              If less than two items are provided, returns None for both to avoid division by zero errors on empty sets in a robust manner, though standard arithmetic handles single elements fine (average equals itself). For this specific task requirement of 'multiple', we assume input will have more than one, but handle edge cases gracefully.
    """
    total = sum(volume_measurements)

    # Calculate average safely. If list is empty or has one element, it still works mathematically.
    if len(volume_measurements) > 0:
        average = statistics.mean(volume_measurements)
    else:
        # Fallback for strictly zero inputs which shouldn't happen based on task description of "multiple" but ensures runtime safety.
        return total, None

    return total, average

def main():
    """
    Main function containing the hard-coded sample values as required by the prompt constraints.
    This block runs without user input, command-line arguments, or network access.
    It demonstrates calculating totals and averages for a predefined set of measurements: [500, 750, 1250].
    """

    # Hard-coded sample volume measurements in milliliters (ml)
    # These are valid numeric values representing multiple inputs to satisfy the task context.
    sample_data = [500.0, 750.0, 1250.0]

    result_sum, result_average = calculate_volumes(sample_data)

    if result_average is None:
        print("Total Volume:", result_sum)
        print("Average Volume: Not applicable (insufficient data)")
    else:
        # Display results formatted clearly
        total_str = f"Total Volume: {result_sum} ml"
        avg_str = f"Average Volume: {round(result_average, 2)} ml"

        print(total_str)
        print(avg_str)

if __name__ == '__main__':
    main()