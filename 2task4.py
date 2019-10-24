def clock_face():
    hour1 = 6
    hour2 = 6
    min1 = 1
    min2 = 2
    sec1 = 30
    sec2 = 10

    clock1_in_sec = (hour1 * 60 * 60) + (min1 *60) + sec1 
    clock2_in_sec = (hour2 * 60 * 60) + (min2 * 60) + sec2
    clock3_in_sec = clock2_in_sec - clock1_in_sec
    print(clock3_in_sec)   

clock_face()