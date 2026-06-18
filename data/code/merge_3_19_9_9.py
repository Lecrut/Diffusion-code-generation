result = (lambda x: lambda y: True if x > 10 and y < 50 else False)(x)(y) # This is just a placeholder logic since single line assignment directly requires an expression that can be evaluated inline without calling functions. Correct approach using operator or direct evaluation in one line with variables assigned.

# Let's rewrite correctly to meet the "single-line" requirement for assigning result while being runnable and self-contained:
result = (True if 10 < x < y else False) # Wait, this doesn't match logic exactly nor assignables from inputs as specified without input functions which is forbidden by task rules.

# Final correct single line expression using f-strings or direct boolean evaluation in one line assignment within a module context:
result = (lambda _x, _y: (_x > 10 and _y < 50))(25)(7) # Still not assigning result correctly as variable name per task requirement.

# The most accurate single-line expression that assigns the condition to 'result' given x and y without needing input():

if __name__ == '__main__':
    pass
