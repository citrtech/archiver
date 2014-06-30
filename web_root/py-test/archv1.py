from mod_python import apache
from mod_python import psp
from datetime import datetime
from datetime import timedelta
import tempfile

def joinMP3s(files):
	#output = ##find output file name
	output = tempfile.mkstemp(".mp3")
	ofh = open(output[1], 'rb')
	for f in files:
		fh = open(f, 'rb')
		ofh.write(fh.read())
		fh.close()
	ofh.close()
	return output
	
class ArchiveJoiner():
	def __init__(self,startTime,endTime):
                self.__start = time.strptime(startTime, "%d-%m-%Y %H:%M:%S")
                self.__end = time.strptime(endTime, "%d-%m-%Y %H:%M:%S")
		self.__startTime - startTime
		self.__endTime = endTime
		self.__diff = self.__end - self.__start

	def outputMP3(self):
		k = 0
		day = self.__start
		files = []
		if(self.__diff.days <= 1): #just one day or less
			ai = ArchiveInfo(self.__start)
			files.append(ai.getArchiveBetween(self.__startTime, self.__endTime)
		else: #multiple days
		        while k < self.__diff.days: 

class ArchiveInfo():
	def __init__(self,dt=None):
		if dt is None:
			self.__dt = datetime.datetime.now()
		else:
			self.__dt = dt

	def getDT(self):
		return self.__dt

	def getPath(self):
		return "/home/rtav/audio_log/v1/%d/%d/%d" % (self.getDT().year,
							  self.getDT().month,
							  self.getDT().day)
	def getFiles(self):
		files = os.listdir(self.getPath())
		return files
	def getFileTimes(self):
		f = self.getFiles()
		ret = []
		for f in files:
			ret.append(int(f[0:f.index("-")]))

	def getArchiveBetween(self,starTime,endTime):
		files = self.getFilesBetweenTimes(startTime, endTime)
		fps = selfgetFilesFullPaths(files)
		return joinMP3s(fps)

	def getFilesBetweenTimes(self,startTime,endTime):
		ft = self.getFileTimes()
		start = time.strptime(startTime, "%d-%m-%Y %H:%M:%S")
		end = time.strptime(endTime, "%d-%m-%Y %H:%M:%S")
		ret = []
		for t in ft:
			s = time.localtime(t)
			if s > start and s < end:
				ret.append(t)

	def getFilesFullPath(self,files):
		ret = []
		for f in files:
			ret.append("%s/%s" % (self.getPath(), f))
		return ret

class ArchiveRequest():
	def __init__(self,startTime,hours,minutes,seconds):
		self.__start = datetime.strptime(startTime, "%d-%m-%Y %H:%M:%S")
		self.__hours = hours
		self.__minutes = minutes
		self.__seconds = seconds
		self.__ai = ArchiveInfo()

	def getPath(self,dt):
		return self.__ai.getPath(dt)
	
	def getStartTime(self,dt):
		return self.__ai.getStartTime(dt)

	def output(self):
		days = self.__end - self.__start
		#loop over days, 0 is first, days.days - 1 is last
		for day in range(0, days.days):
			start = None
			end = None
			if day == 0:
				start = getStartTime(datetime(self.__start.year,
							      self.__start.month,
							      self.__start.day))
				end = datetime(self.__start.year,
					       self.__start.month,
					       self.__start.day,
					       24,
					       00,
					       00)
				#special day, start from self.__start
			if day == (day - 1):
				#special day, last day, to end
				day = self.__start + (self.__oneday * day)
				start = getStartTime(datetime(day.year,
                                                              day.month,
                                                              day.day))
				end = datetime(day.year,
					       day.month,
					       day.day,
					       self.__end.hours,
					       self.__end.minutes,
					       self.__end.seconds)
					       
			else:
				day = self.__start + (self.__oneday * day)
	                        #otherwise, add day * days to self.__start
				start = getStartTime(datetime(day.year,
                                                              day.month,
                                                              day.day))

				end = datetime(day.year,
					       day.month,
					       day.day,
					       24,
					       0,
					       0)
			#chunk audio from start to end
			chunk = self.__getAudioChunk(start,end)


		
			
		

def outputPSP(req, n):
	req.content_type = "text/html"
        p = psp.PSP(req, "psp/%s.psp" % (n))
        p.run()

def archive(req,starTime,hours,minutes,seconds):
	arch = ArchiveRequest(startTime, hours, minutes, seconds)

def index(req,startTime="17-04-2013 00:00:00"):
	outputPSP(req, "index")


def hello(req, say="NOTHING"):
	outputPSP(req, "hello")