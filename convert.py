import json
import csv
import sys

second_arg = sys.argv[2]

def json_csv(file=second_arg):
    f = open(file)
    
    #load json
    data = json.load(f)
    f.close()

    f = open('data.csv','w+')
    csv_file = csv.writer(f)
    count = 0
  
    for d in data: 
     if count == 0: 
        header = d.keys() 
        csv_file.writerow(header) 
        count = count + 1
     csv_file.writerow(d.values()) 
    
    f.close()
    
def csv_json(file=second_arg):
    
    data = {} 
      
    with open(file) as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    with open('test2.json', 'w') as f:
        json.dump(rows, f)
    
if __name__ == '__main__':
    globals()[sys.argv[1]](sys.argv[2])

    

    
