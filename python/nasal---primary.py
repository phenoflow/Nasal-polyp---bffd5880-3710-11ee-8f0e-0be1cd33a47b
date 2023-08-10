# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2023.

import sys, csv, re

codes = [{"code":"7406000.0","system":"readv2"},{"code":"H11..00","system":"readv2"},{"code":"11744.0","system":"med"},{"code":"14749.0","system":"med"},{"code":"14888.0","system":"med"},{"code":"19742.0","system":"med"},{"code":"31837.0","system":"med"},{"code":"35897.0","system":"med"},{"code":"36229.0","system":"med"},{"code":"4341.0","system":"med"},{"code":"44518.0","system":"med"},{"code":"44934.0","system":"med"},{"code":"4686.0","system":"med"},{"code":"47466.0","system":"med"},{"code":"50528.0","system":"med"},{"code":"56372.0","system":"med"},{"code":"61281.0","system":"med"},{"code":"6411.0","system":"med"},{"code":"69765.0","system":"med"},{"code":"91482.0","system":"med"},{"code":"977.0","system":"med"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('nasal-polyp-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["nasal---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["nasal---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["nasal---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
