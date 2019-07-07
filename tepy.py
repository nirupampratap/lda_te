def te_stemmer(word):
    
    if(word.endswith("ల") == True or
      word.endswith("ఓ") == True):
        return word[:len(word)-1]    
    
    if(word.endswith("డు") == True or
        word.endswith("ము") == True or
        word.endswith("వు") == True or
        word.endswith("లు") == True or
        word.endswith("ని") == True or
        word.endswith("ను") == True or
        word.endswith("చే") == True or
        word.endswith("తో") == True or
        word.endswith("కై") == True or
        word.endswith("లో") == True or
        word.endswith("కు") == True or
        word.endswith("కి") == True):
        return word[:len(word)-2]
    
    if(word.endswith("చేత") == True or
        word.endswith("తోడ") == True or
        word.endswith("వలన") == True or
        word.endswith("ఓరీ") == True or
        word.endswith("ఓయీ") == True or
        word.endswith("ఓసీ") == True):
        return word[:len(word)-3]
    
    if(word.endswith("లోపల") == True or
        word.endswith("కంటె") == True):
        return word[:len(word)-4]
    
    if(word.endswith("కొఱకు") == True or
        word.endswith("కొరకు") == True or
        word.endswith("పట్టి") == True or
        word.endswith("యొక్క") == True):
        return word[:len(word)-5]
    
    if(word.endswith("గూర్చి") == True):
        return word[:len(word)-6]
       
    if(word.endswith("గురించి") == True):
        return word[:len(word)-7]
    
    if(word.startswith("ఓ") == True):
        return word[1:]
    
    if(word.startswith("ఓయీ") == True or 
      word.startswith("ఓరీ") == True or
      word.startswith("ఓసీ") == True):
        return word[3:]
    
    return word