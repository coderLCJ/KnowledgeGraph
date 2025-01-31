#
# Autogenerated by Thrift Compiler (0.18.1)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py
#

from thrift.Thrift import TType, TMessageType, TFrozenDict, TException, TApplicationException
from thrift.protocol.TProtocol import TProtocolException
from thrift.TRecursive import fix_spec

import sys

from thrift.transport import TTransport
all_structs = []


class Request(object):
    """
    Attributes:
     - Models
     - currentId
     - requestType
     - extendInfo

    """


    def __init__(self, Models=None, currentId=None, requestType=None, extendInfo=None,):
        self.Models = Models
        self.currentId = currentId
        self.requestType = requestType
        self.extendInfo = extendInfo

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.LIST:
                    self.Models = []
                    (_etype3, _size0) = iprot.readListBegin()
                    for _i4 in range(_size0):
                        _elem5 = iprot.readString().decode('utf-8', errors='replace') if sys.version_info[0] == 2 else iprot.readString()
                        self.Models.append(_elem5)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I64:
                    self.currentId = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I64:
                    self.requestType = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.MAP:
                    self.extendInfo = {}
                    (_ktype7, _vtype8, _size6) = iprot.readMapBegin()
                    for _i10 in range(_size6):
                        _key11 = iprot.readString().decode('utf-8', errors='replace') if sys.version_info[0] == 2 else iprot.readString()
                        _val12 = iprot.readString().decode('utf-8', errors='replace') if sys.version_info[0] == 2 else iprot.readString()
                        self.extendInfo[_key11] = _val12
                    iprot.readMapEnd()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('Request')
        if self.Models is not None:
            oprot.writeFieldBegin('Models', TType.LIST, 1)
            oprot.writeListBegin(TType.STRING, len(self.Models))
            for iter13 in self.Models:
                oprot.writeString(iter13.encode('utf-8') if sys.version_info[0] == 2 else iter13)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.currentId is not None:
            oprot.writeFieldBegin('currentId', TType.I64, 2)
            oprot.writeI64(self.currentId)
            oprot.writeFieldEnd()
        if self.requestType is not None:
            oprot.writeFieldBegin('requestType', TType.I64, 3)
            oprot.writeI64(self.requestType)
            oprot.writeFieldEnd()
        if self.extendInfo is not None:
            oprot.writeFieldBegin('extendInfo', TType.MAP, 4)
            oprot.writeMapBegin(TType.STRING, TType.STRING, len(self.extendInfo))
            for kiter14, viter15 in self.extendInfo.items():
                oprot.writeString(kiter14.encode('utf-8') if sys.version_info[0] == 2 else kiter14)
                oprot.writeString(viter15.encode('utf-8') if sys.version_info[0] == 2 else viter15)
            oprot.writeMapEnd()
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class Response(object):
    """
    Attributes:
     - errCode
     - errMsg
     - predictResults

    """


    def __init__(self, errCode=0, errMsg=None, predictResults=None,):
        self.errCode = errCode
        self.errMsg = errMsg
        self.predictResults = predictResults

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.I64:
                    self.errCode = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.errMsg = iprot.readString().decode('utf-8', errors='replace') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.MAP:
                    self.predictResults = {}
                    (_ktype17, _vtype18, _size16) = iprot.readMapBegin()
                    for _i20 in range(_size16):
                        _key21 = iprot.readString().decode('utf-8', errors='replace') if sys.version_info[0] == 2 else iprot.readString()
                        _val22 = iprot.readString().decode('utf-8', errors='replace') if sys.version_info[0] == 2 else iprot.readString()
                        self.predictResults[_key21] = _val22
                    iprot.readMapEnd()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('Response')
        if self.errCode is not None:
            oprot.writeFieldBegin('errCode', TType.I64, 1)
            oprot.writeI64(self.errCode)
            oprot.writeFieldEnd()
        if self.errMsg is not None:
            oprot.writeFieldBegin('errMsg', TType.STRING, 2)
            oprot.writeString(self.errMsg.encode('utf-8') if sys.version_info[0] == 2 else self.errMsg)
            oprot.writeFieldEnd()
        if self.predictResults is not None:
            oprot.writeFieldBegin('predictResults', TType.MAP, 3)
            oprot.writeMapBegin(TType.STRING, TType.STRING, len(self.predictResults))
            for kiter23, viter24 in self.predictResults.items():
                oprot.writeString(kiter23.encode('utf-8') if sys.version_info[0] == 2 else kiter23)
                oprot.writeString(viter24.encode('utf-8') if sys.version_info[0] == 2 else viter24)
            oprot.writeMapEnd()
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(Request)
Request.thrift_spec = (
    None,  # 0
    (1, TType.LIST, 'Models', (TType.STRING, 'UTF8', False), None, ),  # 1
    (2, TType.I64, 'currentId', None, None, ),  # 2
    (3, TType.I64, 'requestType', None, None, ),  # 3
    (4, TType.MAP, 'extendInfo', (TType.STRING, 'UTF8', TType.STRING, 'UTF8', False), None, ),  # 4
)
all_structs.append(Response)
Response.thrift_spec = (
    None,  # 0
    (1, TType.I64, 'errCode', None, 0, ),  # 1
    (2, TType.STRING, 'errMsg', 'UTF8', None, ),  # 2
    (3, TType.MAP, 'predictResults', (TType.STRING, 'UTF8', TType.STRING, 'UTF8', False), None, ),  # 3
)
fix_spec(all_structs)
del all_structs
