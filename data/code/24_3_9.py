if __name__ == '__main__':
    x = -5  # Sample negative value -> True
    assert (x < 0) is True, "Expression failed"
    
    y = 10   # Sample non-negative value -> False
    assert (y < 0) is False, "Expression failed for positive number"