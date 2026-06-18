import json

def calculate_total_volume(objects):
    """
    Calculate the total volume of all objects in a dictionary.

    Args:
        objects (dict): A dictionary where keys represent object types 
                        and values are floats representing their volumes.

    Returns:
        float: The sum of all volume measurements.
    """
    return sum(objects.values())

if __name__ == '__main__':
    sample_data = {
        "box": 10.5,
        "sphere": 4.2,
        "cylinder": 7.8
    }

    total_volume = calculate_total_volume(sample_data)
    
    print(f"The total volume of all objects is: {total_volume}")