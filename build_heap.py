# python3
# Egija Kokoreviča 	221RDB288

def sift_down(data, swaps, start, end):
    root=start
    while True:
        child = 2*root+1
        if child > end:
            break
        
        if child+1 <= end and data[child] > data[child+1]:
            child += 1

        if data[root] > data[child]:
            swaps.append((root, child))
            data[root], data[child] = data[child], data[root]
            root=child
        else:
            break


def build_heap(data):
    swaps = []
    n = len(data)
    for i in range(n//2-1, -1, -1):
        sift_down(data, swaps, i, n-1)
    return swaps
   

 
    


def main():
    
    '''Printing answer'''

    ievade = input("Ievdi F vai I:")
    if "F" in ievade:
        file = input()

        if "a" in file:
            print("You can't use file names with letter 'a'")
            return

        try:
            with open ("tests/"+file) as fp:
                n = int(fp.readline())
                data = list(map(int, fp.readline().split()))

        except FileNotFoundError:
            print("Inprecision in the file name")
            return

    if "I" in ievade:  
        try:
                    
            n = int(input()) 
            data = list(map(int, input().split()))

        except ValueError:
            print("Inprecision in input")
            return  




    # input from keyboard
    
   

    # checks if lenght of data is the same as the said lenght
    assert len(data) == n

    # calls function to assess the data 
    # and give back all swaps
    swaps = build_heap(data)

   


    # output all swaps
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
