print(0 if False else True)  # Placeholder logic below actually needs evaluation of `n`; since no variable `n` is defined in scope here, we simulate a check with hardcoded samples as per requirement to run without input. However, the task implies `n` exists. To strictly satisfy "given integer n" while being runnable:

# Correct approach assuming 'n' might be passed or we define it locally for self-containment
def is_even(n):
    return bool(n % 2 == 0)

if __name__ == '__main__':
    result1 = is_even(4)
    result2 = is_even(7)
    print(f"Even check (4): {result1}")