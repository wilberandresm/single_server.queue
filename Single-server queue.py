import numpy as np
from re import findall

def read():
    data = []
    with open("data.txt") as d:
        for i in d.readlines():
            data.append(findall(r"[\d]+.[\d]+", i))
    return np.array(data, dtype=float)

if __name__ == "__main__":

    data = read()
    a = data[:,0]
    s = data[:,1]
    d = []; c = []; Co = 0; i = 0; n = len(a)
    while(i<n):
        if(a[i]<Co):
            d.append(Co-a[i])
        else:
            d.append(0)
        c.append(a[i]+d[i]+s[i])
        Co = c[i]
        i+=1

    #Job-Averaged Statistics
    a_inter = a[n-1]/n #Average interarrival time
    a_s = sum(s)/n #Average service time
    a_d = sum(d)/n #Average delay
    a_w = a_d + a_s
    a_rate = 1/a_inter #Arrival rate
    s_rate = 1/a_s #Service rate

    #Time-Averaged Statistics
    
    time_q = sum(d)/c[len(c)-1] #Time-averaged number in the queue
    time_x = sum(s)/c[len(c)-1] #Time-averaged number in service
    time_l = time_q + time_x #Time-averaged number in the node

    print("Job-Averaged Statistics:")
    print("\nAverage interarrival Time: {0}\nAverage service time: {1}\nAverage delay: {2}".format(a_inter,a_s,a_d))
    print("Recall: {0}\nArrival rate: {1}\nService rate: {2}".format(a_w,a_rate,s_rate))
    print("\nTime-Averaged Statistics:")
    print("\nTime-averaged number in the queue:",time_q)
    print("Time-averaged number in service:",time_x)
    print("Time-averaged number in the node:",time_l)