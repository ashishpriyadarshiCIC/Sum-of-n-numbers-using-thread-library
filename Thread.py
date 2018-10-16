
import threading
 
def print_num():
   
    sum1 = 0

    num =  10

    for i in range(num):
        sum1 = sum1 + i

    print("Sum is :"  + str(sum1))

    print("Thread1 Done.")

def print_thread2():
   
    print("Hello")
    print("Thread2 Done.")        
 
if __name__ == "__main__":

    t1 = threading.Thread(target=print_num)
    t2 = threading.Thread(target=print_thread2)
 

    t1.start()

    t2.start()
 

    t1.join()

    t2.join()
 

    print("Completed....")
