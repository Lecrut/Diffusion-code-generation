def compare_volumes(file_path):
    try:
        with open(file_path, 'r') as file:
            volumes = file.readlines()
        
        if len(volumes) != 2:
            raise ValueError("The file must contain exactly two volume measurements.")
        
        volume1 = float(volumes[0].strip())
        volume2 = float(volumes[1].strip())
        
        if volume1 > volume2:
            return "First volume is larger."
        elif volume2 > volume1:
            return "Second volume is larger."
        else:
            return "Both volumes are equal."
    
    except FileNotFoundError:
        return "File not found."
    except ValueError as e:
        return str(e)
    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == '__main__':
    result = compare_volumes('volumes.txt')
    print(result)