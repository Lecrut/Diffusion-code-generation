if __name__ == '__main__':
    x = 5 if True else -3
    
# Test with positive value (should be True)
result1 = "True" if x > 0 else "False"
assert result1 == "True", f"Expected 'True', got '{result1}'"

x = -7
result2 = "True" if x > 0 else "False"
assert result2 == "False", f"Expected 'False', got '{result2}'"

print("All assertions passed.")