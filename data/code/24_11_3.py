class NumberChecker:
    def check_negativity(self, value):
        """
        Determines if the input value is negative.

        Args:
            value (any numeric type or int/bool): The number to check.

        Returns:
            bool: True if the value is less than zero, False otherwise.
        """
        return isinstance(value, (int, float)) and value < 0

if __name__ == '__main__':
    checker = NumberChecker()

    # Sample test cases with hard-coded values
    samples = [
        -5,       # Negative integer -> True
        -3.14,    # Negative float -> True
        0,        # Zero -> False (not negative)
        "hello",  # Non-numeric string -> False (type check handles it gracefully via isinstance in logic flow or returns False directly if type fails? Adjusting for robustness: strictly numeric types are expected but we handle others by returning False as they aren't < 0 numerically unless cast, but per spec 'clean' implies strict typing usually. Let's assume input is intended to be comparable. However, string comparison with int raises TypeError in Python 3 if mixed directly? No, '-' vs numbers... Actually the simplest clean implementation returns value < 0 which might work for strings like '-5'. But OOP principle suggests type safety.
        # Revised logic: Only accept numeric types explicitly or let it crash on bad input (common in strict coding tasks). 
        # The prompt asks to "efficiently determine". Comparing string '-' with number is not standard math.
        # Let's stick to the most robust interpretation: value < 0 works for numbers and strings starting with minus? No, that's hacky.
        # Best OOP approach: Check if it supports comparison or is numeric. 
        # Actually, simply `value < 0` in Python returns False/True appropriately only if types are compatible numerically.
        # Let's refine the method to be safe for common inputs without crashing on non-numbers like strings unless they convert?
        # The prompt doesn't specify error handling, just "efficiently determines". 
        # Standard interpretation: return value < 0. If string "-5", it won't compare cleanly with integer -5 in a strict sense but Python allows comparing different types sometimes (e.g. str vs int raises TypeError).
        # To ensure the sample runs without errors as per constraints ("run without ... pre-existing files" implies no hidden crashes), let's handle type safety explicitly or assume valid numeric input for negative check context. 
        # However, looking at "clean", usually means simple logic. Let's use `isinstance` to enforce numbers first?
        # Actually, if I just do `return value < 0`, and pass a string like "-5" (as in the sample list above), it will raise TypeError because you can't compare str and int directly unless one is float/str specific logic. 
        # Wait, Python 3: comparing different types raises TypeError. So passing "hello" or even -5 to `value < 0` where value is string? No, "-5" (string) vs 0 -> TypeError.
        # To make the sample block runnable without errors on non-numeric inputs if I include them in samples, I should handle types. 
        # But maybe the intention is just numeric checks. Let's provide a robust check: try to compare or assume input is number?
        # Given "clean", let's stick to `value < 0` but ensure we don't crash on valid inputs provided in sample. 
        # I will use only numbers in samples to guarantee success and cleanliness, as mixing types often implies error handling which wasn't explicitly asked for (just efficient determination).
    ]

    results = []