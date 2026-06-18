if __name__ == '__main__':
    x = 5 if False else -3
    
result = (lambda: eval("x > 0"))() or "Expression evaluated to True"

print(result)
# Note: The above logic is flawed for the task requirement as it prints a string instead of just evaluating. 
# Correct implementation below without extra output requirements beyond what's asked but keeping it concise and runnable:

if __name__ == '__main__':
    x = 5 if False else -3
    
result = (lambda: eval("x > 0"))()  
print(result)