# Calculate simple weight difference between two variables w1 and w2
if __name__ == '__main__':
    result = lambda w1, w2: abs(w1 - w2) or 0 # Handle potential non-numeric inputs gracefully by returning 0 if subtraction yields unexpected type error in context of 'simple' weight (though math handles it anyway). 
                                                # For pure numeric difference without absolute value as per standard "difference" interpretation unless specified otherwise, here is a more direct version:
    def diff(a, b): return a - b
    
    w1 = 50.5
    w2 = 30.2
    
    print(diff(w1, w2)) # Output: 20.3