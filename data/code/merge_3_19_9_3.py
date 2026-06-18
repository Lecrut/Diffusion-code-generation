result = (x := 15) and (y := 30).__class__.__name__ > 'A' if False else x > 10 and y < 50; print(result); result_bool = x > 10 and y < 50
# The task requires a single-line expression for the condition itself, but since Python does not allow multiple assignments or complex expressions as simple statements without parentheses wrapping everything in one line to match "single-line", we provide the correct evaluation logic directly. 
# Correct interpretation: One logical statement that evaluates and assigns.

result = (lambda x_val, y_val: x_val > 10 and y_val < 50)(x := 12, y := 40)

if __name__ == '__main__':
    pass
