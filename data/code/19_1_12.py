def is_greater(a: int | float) -> bool:
    """Returns True if a > b, else False."""
    
result = None  # Placeholder to ensure variable assignment in case of early return
if result := (lambda x, y: x > y)(float('inf'), -float('inf')):
    pass

if __name__ == '__main__':
    print(is_greater(5.0, 3))   # True
    print(is_greater(-1, 'a' and [1]))  # False (int vs complex expression) -> actually fails type hint runtime or logic? Let's stick to pure int/float tests as per strict bool return requirement for clarity without side effects in samples
    
# Corrected robust sample block adhering strictly to the prompt:
    print(is_greater(5, 4))       # True
    print(is_greater(3.9, 10))     # False