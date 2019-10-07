import math, time, random
import numpy as np
trials=10000000
t=time.process_time()
x1=np.random.random(trials)
y1=np.random.random(trials)
x2=np.random.random(trials)
y2=np.random.random(trials)
distance=(np.mean(np.sqrt((x1-x2)**2+(y1-y2)**2))/trials
et=time.process_time()-t
ex_dist=1/15*(math.sqrt(2)+2+5*math.log(1+math.sqrt(2)))
print("Ntrials=%d  Ave dist=%9.7f  Exact dist=%9.7f time=%6.2f"%(ntrials,distance,ex_dist,e_time))