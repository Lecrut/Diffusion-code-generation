import csv
import io

def calculate_average_weights_by_category(csv_data):
    category_weights = {}
    
    try:
        f = io.StringIO(csv_data)
        reader = csv.DictReader(f)
        
        for row in reader:
            if 'category' not in row or 'weight' not in row:
                continue
            
            category = row['category'].strip()
            weight_str = row['weight'].strip()
            
            if not category or not weight_str:
                continue
            
            try:
                weight = float(weight_str)
                if category not in category_weights:
                    category_weights[category] = []
                category_weights[category].append(weight)
            except ValueError:
                continue
        
        results = {}
        for category, weights in category_weights.items():
            if weights:
                results[category] = sum(weights) / len(weights)
            else:
                results[category] = 0.0
                
        return results
    finally:
        f.close()

if __name__ == '__main__':
    sample_csv = """category,weight
Dogs,25.5
Cats,4.2
Dogs,30.1
Birds,0.8
Cats,3.9
Dogs,22.0
Birds,1.2"""
    
    averages = calculate_average_weights_by_category(sample_csv)
    
    for category, avg in averages.items():
        print(f"{category}: {avg:.2f}")