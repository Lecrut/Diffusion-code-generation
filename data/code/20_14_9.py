def compare_items(a: object, b: object) -> bool:
    """
    Compares two items first by checking if their types are identical.
    If the types match, it proceeds to check value equality using ==.
    
    Args:
        a: First item to be compared.
        b: Second item to be compared.
        
    Returns:
        bool: True if both types and values are equal; False otherwise.
    """
    type_check = type(a) is type(b)
    return type_check and (a == b)

if __name__ == '__main__':
    pass
