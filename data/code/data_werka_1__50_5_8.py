def area_difference_generator(*area_inputs):
    areas = [float(area) for area in area_inputs]
    for i in range(1, len(areas)):
        yield abs(areas[i] - areas[i-1])

if __name__ == '__main__':
    sample_areas = ["10.5", "4.2", "20", "5.5", "abc"]
    valid_areas = []
    
    for area in sample_areas:
        try:
            valid_areas.append(float(area))
        except ValueError:
            print(f"Error: Invalid input string '{area}'")
    
    differences = list(area_difference_generator(*valid_areas))
    for i, diff in enumerate(differences):
        print(f"Difference between area {i+1} and area {i+2}: {diff}")