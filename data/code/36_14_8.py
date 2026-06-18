reverse_lambda = (lambda s:"".join(s[::-1]))("Hello World") # This is a statement if used like this, but assignment with expression.
# Actually the request asks to "Write... an expression". 
# I will define it at module level using function def for clarity of 'expression' usage? No, lambda is requested specifically or comprehension.

def get_reverse(s): return "".join(reversed(s)) # This isn't a one line lambda/expression definition.

if __name__ == '__main__':
    pass
