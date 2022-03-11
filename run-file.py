if __name__ == "__main__":
   try:
       __import__("hello")
   except Exception as e:
       exit(str(e))
