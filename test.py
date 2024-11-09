try:
    f = open("demo.txt","wt")
    try:
        f.write("This is added text")
    except:
        print("Something went wrong when writing to the file")
    finally:
        f.close()
except:
    print("Something went wrong when opening to the file")