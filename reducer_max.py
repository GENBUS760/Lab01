#!/usr/bin/env python3

import sys

def reducer():
    sales_max = 0
    oldKey = None

    for line in sys.stdin:
        data = line.strip().split(",")

        thisKey, thisCost = data
        if oldKey is not None and oldKey != thisKey:
            print(oldKey + "," + str(sales_max))
            sales_max = 0

        oldKey = thisKey
        sales += float(thisCost)
        sales_max = max(sales_max, sales)

    if oldKey is not None: # for the final key
        print (oldKey + "," + str(sales_max))

if __name__ == "__main__":
    # what function should run when python reducer.py is called?
    reducer()
