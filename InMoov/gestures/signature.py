def signature():
  i01.startedGesture()
  ##approach
  i01.setHeadVelocity(31.0,31.0,-1,-1,-1)
  i01.setArmVelocity("left",31.0,31.0,31.0,31.0)
  i01.setArmVelocity("right",31.0,31.0,31.0,31.0)
  i01.setHandVelocity("left",31.0,31.0,31.0,31.0,31.0,31.0)
  i01.setHandVelocity("right",31.0,31.0,31.0,31.0,31.0,31.0)
  i01.moveHead(0,102,90,90,74)
  i01.moveArm("left",84,73,49,10)
  i01.moveArm("right",82,67,45,24)
  i01.moveHand("left",2,2,2,2,2,120)
  i01.moveHand("right",180,180,180,179,180,165)
  sleep(2)
  ##approach left hand
  i01.moveHead(0,83,90,90,74)
  i01.moveArm("left",70,65,55,10)
  i01.moveArm("right",101,67,63,24)
  i01.moveHand("left",2,2,2,2,2,120)
  i01.moveHand("right",180,180,180,179,180,165)
  sleep(2)
  ##approach pen
  i01.moveHead(0,83,90,90,74)
  i01.moveArm("left",70,50,55,10)
  i01.moveArm("right",79,45,72,24)
  i01.moveHand("left",2,2,2,2,2,120)
  i01.moveHand("right",180,180,180,179,180,165)
  sleep(2)
  ##4
  i01.moveHead(0,83,90,90,74)
  i01.moveArm("left",77,50,55,10)
  i01.moveArm("right",79,45,72,24)
  i01.moveHand("left",2,2,2,2,2,120)
  i01.moveHand("right",180,180,180,179,180,165)
  sleep(2)
  ##approach pen bis
  i01.moveHead(0,83,90,90,74)
  i01.moveArm("left",77,50,60,10)
  i01.moveArm("right",85,43,72,24)
  i01.moveHand("left",2,2,2,2,2,120)
  i01.moveHand("right",180,180,180,179,180,165)
  sleep(2)
  ##4bis
  i01.moveHead(0,83,90,90,74)
  i01.moveArm("left",77,50,55,10)
  i01.moveArm("right",79,45,72,24)
  i01.moveHand("left",2,2,2,2,2,120)
  i01.moveHand("right",180,180,180,179,180,165)
  sleep(2)
  ##5
  i01.moveHead(0,83,90,90,74)
  i01.moveArm("left",77,50,55,10)
  i01.moveArm("right",79,45,72,24)
  i01.moveHand("left",2,2,2,2,2,110)
  i01.moveHand("right",180,180,180,179,180,165)
  sleep(2)
  ##6
  i01.moveHead(0,83,90,90,74)
  i01.moveArm("left",78,50,60,10)
  i01.moveArm("right",78,45,72,24)
  i01.moveHand("left",2,2,2,2,2,110)
  i01.moveHand("right",180,180,180,179,180,165)
  sleep(2)
  ##7
  i01.moveHead(0,83,90,90,74)
  i01.moveArm("left",78,61,60,10)
  i01.moveArm("right",86,69,72,21)
  i01.moveHand("left",2,2,2,2,2,110)
  i01.moveHand("right",180,180,180,179,180,165)
  sleep(2)
  ##8
  i01.moveHead(0,83,90,90,74)
  i01.moveArm("left",78,50,60,10)
  i01.moveArm("right",86,79,72,21)
  i01.moveHand("left",2,2,2,2,2,110)
  i01.moveHand("right",180,180,180,179,180,165)
  sleep(2)
  ##9
  i01.moveHead(0,83,90,90,74)
  i01.moveArm("left",78,50,60,10)
  i01.moveArm("right",52,91,72,21)
  i01.moveHand("left",2,2,2,2,2,110)
  i01.moveHand("right",180,180,180,179,180,68)
  sleep(2)
  ##10
  i01.moveHead(45,69,90,90,74)
  i01.moveArm("left",78,50,60,10)
  i01.moveArm("right",52,91,32,9)
  i01.moveHand("left",2,2,2,2,2,110)
  i01.moveHand("right",180,180,180,179,180,112)
  sleep(2)
  ##11
  i01.moveHead(45,88,90,90,74)
  i01.moveArm("left",49,52,75,0)
  i01.moveArm("right",52,91,32,9)
  i01.moveHand("left",2,2,2,2,2,180)
  i01.moveHand("right",180,180,180,179,180,112)
  i01.mouth.speakBlocking("there you go")
  #i01.mouth.speakBlocking(u"Туда вы идёте")
  sleep(1)
  i01.finishedGesture()
