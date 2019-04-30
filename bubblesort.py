def bubble_sort(list):
    
    for num in range(len(list)-1, 0, -1):

        is_sorted = False 
        while is_sorted == False:
            num_swaps = 0   
            for i in range(num):
                if list[i]>list[i+1]:
                      
                    num_swaps += 1   
                    temp = list[i]
                    list[i] = list[i+1]
                    list[i+1] = temp
            
            if num_swaps == 0:
                is_sorted = True
            
    return list

def main():
    
    list = [15, 11, 22, 987, 14, 2]
    
    print(bubble_sort(list))

if __name__ == "__main__":
    main()
