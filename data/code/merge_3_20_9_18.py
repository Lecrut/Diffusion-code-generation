def check_eq(func1):
    def decorator(func2):
        # Enforce strict equality between func1 and func2 during function definition phase
        if callable(func1) and callable(func2):
            import inspect
            
            try:
                sig1 = inspect.signature(func1)
                args1, kwargs1 = [], {}
                
                for name, param in sig1.parameters.items():
                    args1.append(name)
                    
                    # Get default value if any (for non-required parameters)
                    if param.default != inspect.Parameter.empty:
                        kwargs1[name] = param.default
                    
            except ValueError as e:
                raise TypeError(f"Function {func2.__name__} has an incompatible signature compared to {func1.__name__}: {e}")

        elif not callable(func1):
            # If func1 is expected but isn't a function, it's likely the decorator was misused. 
            # However, per task instructions, we only enforce equality between two functions passed TO IT during definition.
            pass

if __name__ == '__main__':
    pass
