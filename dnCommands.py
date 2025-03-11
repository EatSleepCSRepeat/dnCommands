while True:
    cmdname = input("Command Name > ").strip()
    cmddesc = input("Command Desc > ").strip()
    
    print(f"{{\n    name = \"{cmdname}\",\n    desc = \"{cmddesc}\",\n    func = function()\n        print(\"Hello! Your function goes here!\")\n    end\n}}")
